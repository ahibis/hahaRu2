//пост запрос через Ajax с объектом данных
function post(Url, data = {}) {
    return new Promise((resolve, reject) => {
        $.post('/' + Url, data, (Data) => {
            resolve(Data);
        });
    })
}
//get запрос через Ajax с объектом данных
function get(Url, data = {}) {
    return new Promise((resolve, reject) => {
        $.get('/' + Url, data, (Data) => {
            resolve(Data);
        });
    })
}
//запрос через Ajax с объектом данных по адресу api/method
function api(method, data = {}) {
    return new Promise((resolve, reject) => {
        $.post('/api/' + method, data, (Data) => {
            resolve(Data);
        });
    })
}
function registration() {
    let form = {};
    $("#auth input").each(function () {
        let el = $(this);
        let name = el.attr("name");
        if (name) {form[name]=el.val()}
    })
    post("Registration/Registration", form).then(r => {
        console.log(r);
        $("#message").text(r.text)
        if(r.status=="ok") location.href="/"
    })
}
function login() {
    let form = {};
    $("#auth input").each(function () {
        let el = $(this);
        let name = el.attr("name");
        if (name) { form[name] = el.val() }
    })
    post("Auth/Login", form).then(r => {
        console.log(r);
        $("#message").text(r.text)
        if (r.status == "ok") location.href = "/"
    })
}
my = {};
$(document).ready(async function () {
    my = await api("getMy");
    my = JSON.parse(my);
    if (!my.Login) $("#userLink").attr("href", "/Auth");  
    my.Login = (my.Login || "авторизоваться");
    $("#userName").text(my.Login);
    my.AvatarSrc = my.AvatarSrc || "/img/logo.png";
    $("#userImg").attr("src", my.AvatarSrc);
})

function sendFiles(Url, DATA={}) {
    return new Promise(resolve => {
        let el=document.createElement("input");
        el.type="file"
        el.multiple=true;
        el.click()
        el.onchange=function(){
           files = el.files;
            var data = new FormData();
            $.each(files, function (key, value) {
                data.append(key, value);
            });
            data.append('my_file_upload', 1);
            for (key in DATA) {
                data.append(key, DATA[key])
            }
            $.ajax({
                url: Url,
                type: 'POST', // важно!
                data: data,
                cache: false,
                //dataType    : 'json',
                processData: false,
                contentType: false,
                success: function (answer, status, jqXHR) {// ОК - файлы загружены
                    resolve(answer)
                },
                error: function (jqXHR, status, errorThrown) {// функция ошибки ответа сервера
                    console.log('ОШИБКА AJAX запроса: ' + status, jqXHR);
                }
            }); 
        }
    })
}
function sendFiles2(element, Url, func) {
    files = element.files;
    var data = new FormData();
    $.each(files, function (key, value) {
        data.append(key, value);
    });
    data.append('my_file_upload', 1);
    $.ajax({
        url: Url,
        type: 'POST', // важно!
        data: data,
        cache: false,
        //dataType    : 'json',
        processData: false,
        contentType: false,
        success: function (answer, status, jqXHR) {// ОК - файлы загружены
            console.log(answer)
            func(JSON.parse(answer))
        },
        error: function (jqXHR, status, errorThrown) {// функция ошибки ответа сервера
            console.log('ОШИБКА AJAX запроса: ' + status, jqXHR);
        }
    });
}
function sendImg(Url,img, DATA={}) {
    return new Promise(resolve => {
        let el=document.createElement("input");
        el.type="file"
        el.multiple=true;
        el.click()
        el.onchange=function(){
           files = el.files;
            var data = new FormData();
            $.each(files, function (key, value) {
                data.append(key, value);
            });
            data.append('my_file_upload', 1);
            for (key in DATA) {
                data.append(key, DATA[key])
            }
            $.ajax({
                url: Url,
                type: 'POST', // важно!
                data: data,
                cache: false,
                //dataType    : 'json',
                processData: false,
                contentType: false,
                success: function (answer, status, jqXHR) {// ОК - файлы загружены
                    resolve(answer)
                },
                error: function (jqXHR, status, errorThrown) {// функция ошибки ответа сервера
                    console.log('ОШИБКА AJAX запроса: ' + status, jqXHR);
                }
            }); 
        }
    })
}