const $ = window.$;
$.get('https://swap-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('DIV#character').text(data.name);
});
