# fampay-assignment

## Goal:

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Tech Stack:

Django, DRF, Celery, Redis, Docker

## Steps to Setup:

- Clone the repository
- Run command: `bash sudo docker-compose up -d --build `
- Access the server at <a href="http://localhost:1337/">localhost:1337</a>

## API Endpoints:

```http
GET /getVideos
```

| Parameter | Type      | Description                                                   |
| :-------- | :-------- | :------------------------------------------------------------ |
| `page`    | `integer` | **Optional**. Page number for the response data, default is 1 |

```http
GET /searchVideoTitle
```

| Parameter | Type      | Description                                                   |
| :-------- | :-------- | :------------------------------------------------------------ |
| `page`    | `integer` | **Optional**. Page number for the response data, default is 1 |
| `title`   | `string`  | **Required**. Matching text in video title                    |

```http
GET /searchVideoDescription
```

| Parameter     | Type      | Description                                                   |
| :------------ | :-------- | :------------------------------------------------------------ |
| `page`        | `integer` | **Optional**. Page number for the response data, default is 1 |
| `description` | `string`  | **Required**. Matching text in video description              |

## Response

```json
{
  "lastPage": 1,
  "pageNumber": 1,
  "numberOfItems": 1,
  "items": [
    {
      "model": "youtube_api.video",
      "pk": 33,
      "fields": {
        "video_id": "99iwUPVKZEM",
        "video_title": "A Lua se Move Todas as Noites — e 10 Novos Fatos Espaciais",
        "published_date_time": "2022-06-17T20:30:01Z",
        "thumbnail_url": "https://i.ytimg.com/vi/99iwUPVKZEM/default.jpg",
        "description": "Animação criada pelo Incrível. ---------------------------------------------------------------------------------------- Música por Epidemic Sound ..."
      }
    }
  ]
}
```

## Postman

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ed934987139fe6a760d2?action=collection%2Fimport)

- **Postman Collections:** [https://www.getpostman.com/collections/ed934987139fe6a760d2](https://www.getpostman.com/collections/ed934987139fe6a760d2)
