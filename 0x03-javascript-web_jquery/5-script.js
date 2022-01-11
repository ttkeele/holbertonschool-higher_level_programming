const $ = window.$;
$('DIV#add_item').click(function () {
    $('<li>Item</li>').appendTo('UL.my_list');
});
