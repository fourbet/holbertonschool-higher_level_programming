const list = $('UL#list_movies');

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (datas) {
  $.each(datas.results, function (i, data) {
    list.append('<li>' + data.title + '</li>');
  });
});
