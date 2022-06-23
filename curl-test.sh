#!/bin/bash

curl --request POST http://127.0.0.1:5000/api/timeline_post -d 'name=Wei&email=wei.he@mlh.io&content=Test Post' {"content":"test post","created_at":"Mon, 02 May 2022 06:14:30 GMT","email":"wei.he@mlh.io","id":3,"name":"Wei"}

curl -X POST http://127.0.0.1:5000/api/timeline_post -d 'name=Wei&email=wei.he@mlh.io&content=This is just a test.'{"content":"This is just a test.","created_at":"Mon, 02 May 2022 06:15:08 GMT","email":"wei.he@mlh.io","id":4,"name":"Wei"}

curl http://127.0.0.1:5000/api/timeline_post
