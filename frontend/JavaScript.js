fetch('/send_squares/')  // Указываем правильный маршрут
  .then(response => response.json())  // Преобразуем ответ в JSON
  .then(data => {
    console.log(data.squares);  // Доступ к данным
  })
  .catch(error => {
    console.error('Ошибка:', error);  // Обработка ошибок
  });
