"""

curl -X POST -d "username=cfe&password=learncode" http://127.0.0.1:8000/api/auth/token/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEwLCJlbWFpbCI6ImNmZUBnbWFpbC5jb20iLCJleHAiOjE0NzYxMTUxMjN9.9rigAHqC-UMa9BzpMmBDr774FG-1z_Bd0rQ9c0XcfK0

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEwLCJlbWFpbCI6ImNmZUBnbWFpbC5jb20iLCJleHAiOjE0NzYxMTUxMjN9.9rigAHqC-UMa9BzpMmBDr774FG-1z_Bd0rQ9c0XcfK0
" http://127.0.0.1:8000/api/comments/

curl http://127.0.0.1:8000/api/comments/


curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEwLCJlbWFpbCI6ImNmZUBnbWFpbC5jb20iLCJleHAiOjE0NzYxMTg1NjJ9.HYXpZaTvyrPMss5BrLSvyOtk4jVcotxtU017qSHxr6c
" -H "Content-Type: application/json" -d '{"content":"another new try"}' 'http://127.0.0.1:8000/api/comments/create/?slug=new-post-item&type=post'



curl -X POST -d "username=anotheruser&password=anotheruser" http://127.0.0.1:8000/api/auth/token/


anotheruser

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFub3RoZXJ1c2VyIiwidXNlcl9pZCI6MTEsImVtYWlsIjoiYW5vdGhlcnVzZXJAZ21haWwuY29tIiwiZXhwIjoxNDc2MTE4ODk5fQ.QteizNbGMLzlwakc6YNgHft4HOuMHKKz3ZVErcFZR08


curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFub3RoZXJ1c2VyIiwidXNlcl9pZCI6MTEsImVtYWlsIjoiYW5vdGhlcnVzZXJAZ21haWwuY29tIiwiZXhwIjoxNDc2MTE4ODk5fQ.QteizNbGMLzlwakc6YNgHft4HOuMHKKz3ZVErcFZR08
" -H "Content-Type: application/json" -d '{"content":"another new try"}' 'http://127.0.0.1:8000/api/comments/create/?slug=new-post-item&type=post'

"""
