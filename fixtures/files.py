import pytest
from pydantic import BaseModel

from clients.files.files_client import get_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileShema
from fixtures.users import UserFixture



class FilesFixture(BaseModel):
    
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_file(files_client: FilesClient) -> FilesFixture:
    request = CreateFileRequestSchema(upload_file="./testdata/files/pantera.png")
    response = files_client.create_file(request)
    return FilesFixture(
    request = request,
    response = response,
    )





