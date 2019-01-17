function Hclick1()
{
  console.log('Шлепнули по заголовку! Функция Hclick1() из static/vito.js')
  pigga_url = "api/pigga"
  $.getJSON(pigga_url, function(data)
  {
    console.log(data)
    $(pbp).html(data["pigga_said"])
  })
}

function Hclick2()
{
  console.log('Шлепнули по заголовку! Функция Hclick2() из static/vito.js')
  /* p_url = "http://sf-pyw.mosyag.in/m04/api/forecasts" */
  p_url = "api/forecasts"
  pigga_url2 = "api/pigga2"
  $.getJSON(p_url, function(data)
  {
    console.log(data)
    $(pred).html(data["prophecies"])
  })
  $.getJSON(pigga_url2, function(data)
  {
    console.log(data)
    $(pbp).html(data["pigga_said2"])
  })


}