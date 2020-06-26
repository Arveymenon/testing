var document;
var $;
var io;

$(document).ready(function () {
    console.log('Document Ready');
    var socket = io.connect('http://127.0.0.1:5000');

    socket.on('connect', function () {

        $('#send_text').click(function () {

            var message = $('#message')[0].value;
            var sender = Math.round(Math.random() * 100);
            console.log(message);
            console.log(sender);

            socket.emit('send-message', {message: message, sender: sender});
        });
    });

    socket.on('recieve_message', function (message) {
        console.log(message)
        var messageblock = $('div');
        messageblock.add('p').innerHtml = message.message;
        messageblock.add('h4').innerHtml = message.sender;
        $('#chat_room').append(`<div><p>${message.message}</p></div>`);
    });
});