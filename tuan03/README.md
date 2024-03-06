# Docker-Node-Mongo-Redis
## 1. Install Redis, Redis Insight
#### a. Redis

![Redis on WSL](https://i.imgur.com/LcyEUkN.png)
![Redis on Window](https://i.imgur.com/SZeNEuZ.png)

#### b. Redis-Insight
http://localhost:5540
![Redis Insight](https://i.imgur.com/yQogh2x.png)

## 2. CRUD NodeJS (SQL Server or My SQL)

- Dang Ky
![Register](https://i.imgur.com/ngBlqaA.png)

-Dang Nhap
![Login](https://i.imgur.com/JanpuO9.png)

-Them san pham va hien thi
![Product](https://i.imgur.com/AoFxjZ8.png)

![Register Performance](https://i.imgur.com/TLdYF2Q.png)

![Login Performance](https://i.imgur.com/xcyo0QR.png)

![Product Performance](https://i.imgur.com/nNkuOQo.png)

## 3. CRUD Redis

![Redis Register Performance](https://i.imgur.com/UiMmz3S.png)

![Redis Login Performance](https://i.imgur.com/5cGLAzq.png)

![Redis Product Performance](https://i.imgur.com/3kdq2Lr.png)

## 4. CRUD Mongo

![Mongo Register Performance](https://i.imgur.com/E5aqh8n.png)

![Mongo Login Performance](https://i.imgur.com/kA7GSYI.png)

![Mongo Register Performance](https://i.imgur.com/xNowoG4.png)
## 5. Compare and Comment result (MongoDB, Redis, SQL DB)
Với 1 vài dữ liệu nhỏ có thể thấy:

- CRUD với SQLDB thì tốc độ sẽ lâu hơn rất nhiều so với Mongo và Redis.

- CRUD với Mongo có thể thấy giảm được rất nhiều lần so với SQLDB.

- CRUD với Redis thì nhanh hơn 1 tí so với Mongo do đã được cache, với bản chất chung chung nhau, đều sử dụng RAM để lưu trữ và đều là các object (document) chứa nhiều cặp key-value nên tốc độ hơn nhau vài ms.

## Hướng dẫn chạy

- Truy cập file app.js sau đó sửa các giá trị:
  ![Img](https://i.imgur.com/oKzROgk.png)
  - dbHost sẽ là host của mongo
  - dbPort sẽ là port mongo
  - dbName là tên db

- Vào cmd
- Gõ dòng lệnh
    `npm run dev`
