<?php

//php -S localhost:9000
//http://localhost:9000/with_httpOnly.php?username=test&password=password&payload=%3Cscript%3Ealert(document.cookie)%3C/script%3E



if (isset($_GET['username']) && isset($_GET['password']))
{
       $username = $_GET['username'];
       $password = $_GET['password'];

       $payload =  $_GET['payload']; //trying to steal cookie

       if ($username === 'test' && $password === 'password')
       {

           $cookie_name = "my_cookie";
           $cookie_value = "cookie_value_here";
           $expiry = time() + (86400 * 30); // 30 days

           // with httpOnly
           setcookie($cookie_name, $cookie_value, $expiry, '/', '', false, true);

           //without httpOnly
           //setcookie($cookie_name, $cookie_value, $expiry, '/', '', false, false);

           echo "Logged in Successfully";

           //Vulnerable to XSS
           echo $payload;
       }

       else
       {
           echo "Logged in Failure";
       }

}


else
{
   echo "Username Password is missed";
}
?>

