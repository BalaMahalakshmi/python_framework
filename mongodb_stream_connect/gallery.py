# streamlit_gridfs_gallery.py
import streamlit as st
from pymongo import MongoClient
from gridfs import GridFS
from PIL import Image
import io
import mimetypes

st.set_page_config(page_title="GridFS Media Gallery", layout="wide")

# --- CONNECT TO MONGODB ---
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
    client.server_info()  # raises if cannot connect
except Exception as e:
    st.error(f"⚠️ Cannot connect to MongoDB: {e}")
    st.stop()

db = client["gallery"]
fs = GridFS(db)

st.title("🗄️ GridFS Media Gallery")

# --- UPLOAD ---
uploaded = st.file_uploader("Upload image / audio / video", type=["jpg","jpeg","png","gif","mp3","wav","mp4","mov","avi"])
if st.button("Upload"):
    if not uploaded:
        st.error("Please choose a file first.")
    else:
        try:
            data = uploaded.read()                # bytes
            ext = uploaded.name.split(".")[-1].lower()
            # simple type classification
            if ext in ("jpg","jpeg","png","gif"):
                mtype = "image"
            elif ext in ("mp3","wav"):
                mtype = "audio"
            else:
                mtype = "video"

            ctype = mimetypes.guess_type(uploaded.name)[0] or ""
            # store metadata in GridFS file document
            file_id = fs.put(data, filename=uploaded.name, metadata={"type": mtype, "content_type": ctype})
            st.success(f"Uploaded {uploaded.name} (id: {file_id})")
        except Exception as e:
            st.error(f"Upload failed: {e}")

st.markdown("---")

# --- LIST / DISPLAY FILES ---
st.subheader("Stored files")
filter_by = st.selectbox("Filter", ["all","image","audio","video"], index=0)

query = {} if filter_by=="all" else {"metadata.type": filter_by}
files_cursor = db.fs.files.find(query).sort("uploadDate", -1)

for f in files_cursor:
    st.write(f"**{f.get('filename')}**")
    try:
        grid_out = fs.get(f["_id"])
        file_bytes = grid_out.read()
        meta = f.get("metadata", {}) or {}
        ftype = meta.get("type", None)
        content_type = meta.get("content_type", None)

        # display
        if ftype == "image" or (not ftype and f["filename"].split(".")[-1].lower() in ("jpg","jpeg","png","gif")):
            try:
                img = Image.open(io.BytesIO(file_bytes))
                st.image(img, caption=f["filename"], use_column_width=True)
            except Exception as e:
                st.error(f"Cannot display image: {e}")
        elif ftype == "audio" or (not ftype and f["filename"].split(".")[-1].lower() in ("mp3","wav")):
            st.audio(file_bytes, format=content_type or f"audio/{f['filename'].split('.')[-1]}")
        else:
            # fallback to video for anything else
            st.video(file_bytes)

        # delete button (unique key per file)
        if st.button(f"Delete {f['filename']}", key=str(f["_id"])):
            try:
                fs.delete(f["_id"])
                st.success(f"Deleted {f['filename']}")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Delete failed: {e}")

    except Exception as e:
        st.error(f"Could not read file {f.get('filename')}: {e}")
