<!DOCTYPE html>
<html>

<head>
  <meta charset='utf-8'>
  <title>Гороскоп на сегодня</title>

  <link
    rel="stylesheet"
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
    integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
    crossorigin="anonymous"
  />
  
  <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>

  <script type="text/javascript" src="static/vito.js"></script>
  
  <link rel="stylesheet" type="text/css" href="static/vito.css">

</head>
  
<body>
  <div class="container">
    <div class="row">
      <div class="col-3" id="pigga">
        <img onclick="Hclick1()" src="static/BP.jpg" width="200"/>
      </div>
      <div class="col-9">
        <h1>BAD HOROSCOPE</h1>
        <p>Добро пожаловать в Bad Horoscope. Этого парня зовут Лил Пигга.</p>
        <p>Сегодня у нас {{ date }} года и он даст тебе самое точное предсказание!</p>
        <div class="row" id="row_chat">
          <div class="col-1" id="chat">
            <img src="static/chat.jpg" width="50"/>
          </div>
          <div class="col-11">
            <p id="pbp">Щелкай на кнопку ниже, только не по мне!</p>
          </div>
        </div>
      </div>
    </div>
    <div class="row" id="knopka">
      <div class="col-3" id="kn">
        <button onclick="Hclick2()" id="knopka">
          <img src="static/cherep.jpg" width="30"> 
          ПРЕДСКАЗАНИЕ
        </button></p>
      </div>
      <div class="col-9" id="predskazanie">
        <p id="pred"></p>
      </div>
    </div>
  </div>
</body>

</html>