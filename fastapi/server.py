import io

from starlette.responses import Response

from fastapi import FastAPI, File


app = FastAPI(
    title="DeepLabV3 image segmentation",
    description="""Obtain semantic segmentation maps of the image in input via DeepLabV3 implemented in PyTorch.
                           Visit this URL at port 8501 for the streamlit interface.""",
    version="0.1.0",
)
@app.get("/")
def read_root():
    return {"Hello": "World"}


