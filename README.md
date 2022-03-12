# Python image converter

### This project is using FastApi as api framework.

## Api

`GET: ${API_ENDOINT}/image-2-pdf`
`{ base64: SOME_BASE_64_STRING, name: SOME_FILE_NAME_STRING }`

will return a base64 string - that contine a PDF with the given image.
