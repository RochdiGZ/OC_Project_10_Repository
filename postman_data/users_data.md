### API Testing with Postman

http://127.0.0.1:8000/signup/
## Testing 01 with the following raw body (json)
{
    "email": "pierre@gmail.com",
    "password": "secret@django",
    "first_name": "Pierre",
    "last_name": "V."
}

## Testing 02 with the following raw body (json)
{
    "email": "rochdi@gmail.com",
    "password": "secret@django",
    "first_name": "Rochdi",
    "last_name": "G."
}

http://127.0.0.1:8000/login/
## Testing 01 with the following raw body (json)
{
    "email": "pierre@gmail.com",
    "password": "secret@django"
}

## Testing 02 with the following raw body (json)
{
    "email": "rochdi@gmail.com",
    "password": "secret@django"
}

http://127.0.0.1:8000/projects/
## Testing 01 with the following raw body (json)
{
    "title": "JustStreamIt",
    "description": "Développer une interface utilisateur",
    "type": "Front-End",
    "project_contributors": [],
    "issue_related": []
}

http://127.0.0.1:8000/projects/
## Testing 02 with the following raw body (json)
{
    "title": "SoftDesk",
    "description": "Développer une API sécurisée",
    "type": "Back-End",
    "project_contributors": [],
    "issue_related": []
}

http://127.0.0.1:8000/projects/1/users/
## Testing with the following raw body (json)
{
    "permission": "Restricted",
    "role": "Contributor",
    "user": 2,
    "project": 1
}

http://127.0.0.1:8000/projects/1/issues/
## Testing with the following raw body (json)
{
    "title": "P01 Issue01",
    "description": "Description of P01 Issue01",
    "tag": "Bug",
    "priority": "High",
    "status": "ToDo",
    "project": 1,
    "author": 1,
    "assignee": 1
}

http://127.0.0.1:8000/projects/1/issues/1/comments/
## Testing with the following raw body (json)
{
    "description": "Comment 01 of issue 01 for project 01",
    "author": 1,
    "issue": 1
}
