<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'phpmailer/src/Exception.php';
require 'phpmailer/src/PHPMailer-6.6.4.php' ;

$mail = new PHPMailer(true) ;

$mail->CharSet = 'UTF-8';
$mail->setLanguage('ru', 'phpmailer/language/');
$mail->IsHTML(true);

//0m Koz0 nucbMo

$mail->setFrom('bryilyant16@gmail.com', 'Проект');
//Komy omnpa6bume

$mail->addAddress('bryilyant16@gmail.com');

//Tema nucema

$mail->Subject = 'Новый клиент';

$body = '<h1>Новый клиент</h1>'ж
$body .= '<h4>Имя:'.$_POST['name'].'</h4>';  
$body .= '<h4>Телефон:'.$_POST['phone-number'].'</h4>';
$body .= '<h4>Выбор:'.$_POST['input-yacht'].'</h4>';

$mail -> Body = $body;

if (!$mail -> send()) {
    $message = 'Ошибка';
} else {
    $message = 'Данные отправлены';
}

$response = ['message' => $message];
header('Content-type: aplication/json');
echo(json_encode($response));

?>