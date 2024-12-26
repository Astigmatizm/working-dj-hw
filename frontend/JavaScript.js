//fetch('/send_squares/')  // Указываем правильный маршрут
//  .then(response => response.json())  // Преобразуем ответ в JSON
//  .then(data => {
//    console.log(data.squares);  // Доступ к данным
//  })
//  .catch(error => {
//    console.error('Ошибка:', error);  // Обработка ошибок
//  });


const data = 'some important data';
const signature = signData(data);  // Подписываем данные с использованием HMAC

fetch('/my-view/', {
    method: 'POST',
    body: new URLSearchParams({
        'data': data,
        'signature': signature
    })
}).then(response => response.json())
  .then(data => console.log(data));
