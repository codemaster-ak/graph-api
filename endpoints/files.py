import datetime
import json
import os

from fastapi import APIRouter, HTTPException, status

from utils import stack_to_base_colours

router = APIRouter()


@router.get("/", response_model=list)
async def get_all_files():
    dirname = os.path.join(".", "files")
    response = []
    if os.path.exists(dirname):
        files = os.listdir(dirname)
        response = list(map(lambda name: {"name": name[:-5]}, files))
    return response


@router.get("/{file_name}")
async def get_file(file_name: str):
    file_path = os.path.join(".", "files", file_name + ".json")
    if os.path.exists(file_path):
        file = open(file_path, "r")
        content = json.loads(file.read())
        file.close()
        return content
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def save_file(stack: list):
    date = datetime.datetime.now()
    file_name = str(date.day) + "." + str(date.month) + "-" + str(date.hour) + ":" + str(date.minute) + ".json"
    base_colours_stack = stack_to_base_colours(stack)
    files_path = os.path.join(".", "files")
    if not (os.path.exists(files_path) and os.path.isdir(files_path)):
        os.mkdir(files_path)
    file_path = os.path.join(files_path, file_name)
    file = open(file_path, "w+")
    content = json.dumps(base_colours_stack)
    file.write(content)
    file.close()
    return {"name": file_name[:-5]}


@router.put("/{file_name}")
async def update_file(file_name: str, stack: list):
    stack = stack_to_base_colours(stack)
    file_path = os.path.join(".", "files", file_name + ".json")
    if os.path.exists(file_path):
        file = open(file_path, "w+")
        content = json.dumps(stack)
        file.write(content)
        file.close()
        return {"detail": 'Success'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")


@router.delete("/{file_name}", status_code=status.HTTP_200_OK)
async def delete_file(file_name: str):
    file_path = os.path.join(".", "files", file_name + ".json")
    if os.path.exists(file_path):
        os.remove(file_path)
        return {"detail": 'Success'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
