from fastapi.testclient import TestClient
from app.main import app
from app.v1.service import tarifa_service, account_service
from app.v1.schema.tarifa_schema import TarifaBase
from app.v1.schema.accounts_schema import AccountCreate
import pytest

@pytest.fixture(scope="session")
def tarifas():
    t = TarifaBase(name = 'Fernando')
    tarifa = tarifa_service.create_tarif(t)
    return tarifa

@pytest.fixture(scope="session")
def accounts(tarifas):
    acc = AccountCreate(
        name = 'Test Account',
        cash = 0,
        warn_limit = 0,
        nobal_limit=0,
        rut='111111',
        type_customer=0,
        id_tarifa=tarifas.id
    )
    account = account_service.create_account(acc)
    return account
    
def test_create_user_ok(accounts):
    client = TestClient(app)
    
    user = {
        'email': 'test_create_user_ok@cosasdedevs.com',
        'username': 'test_create_user_ok',
        'password': 'admin123',
        'account_id': accounts.id
    }
    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data['email'] == user['email']
    assert data['username'] == user['username']

def test_create_user_duplicate_email(accounts):
    client = TestClient(app)

    user = {
        'email': 'test_create_user_duplicate_email@cosasdedevs.com',
        'username': 'test_create_user_duplicate_email',
        'password': 'admin123',
        'account_id': accounts.id
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text

    user['username'] = 'test_create_user_duplicate_email2'

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data['detail'] == 'Email already registered'


def test_create_user_duplicate_username(accounts):
    client = TestClient(app)

    user = {
        'email': 'test_create_user_duplicate_username@cosasdedevs.com',
        'username': 'test_create_user_duplicate_username',
        'password': 'admin123',
        'account_id': accounts.id
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data['detail'] == 'Username already registered'

def test_login(accounts):
    client = TestClient(app)

    user = {
        'email': 'test_login@cosasdedevs.com',
        'username': 'test_login',
        'password': 'admin123',
        'account_id': accounts.id
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text

    login = {
        'username': 'test_login',
        'password': 'admin123'
    }

    response = client.post(
        '/api/v1/login/',
        data=login,
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        allow_redirects=True
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data['access_token']) > 0
    assert data['token_type'] == 'bearer'