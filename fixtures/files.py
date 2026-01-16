import pytest
from clients.files.files_client import get_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestShema, CreateFileResponseShema, FileShema
from fixtures.users import function_user, UserFixture
from pydantic import BaseModel


class FilesFixture(BaseModel):
    
    request: CreateFileRequestShema
    response: CreateFileResponseShema

@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_file(files_client: FilesClient) -> FilesFixture:
    request = CreateFileRequestShema(upload_file="./testdata/files/pantera.png")
    response = files_client.create_file(request)
    return FilesFixture(
    request = request,
    response = response,
    )





