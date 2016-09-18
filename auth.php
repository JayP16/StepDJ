<?php 
$users = array(
    "admin-d"  => "djd",
    "jp"  => "jj"
);
/*
$x = getallheaders();
var_dump($x);
echo $x['Authorization'];
*/

$temp = getallheaders();
$temp = explode(":",$temp['Authorization']);
$uid =  $temp[0];
$pass =  $temp[1];

if (array_key_exists($uid, $users)) {
	if ($pass == $users[$uid]) {
		echo "True";
		return True;
	}	
	else{
		echo "wrong pass";
		return False;
	}
}
else{
	if (isset($uid) && isset($pass)){
		
		echo "user not found";
	}else {
		echo "Only api calls....";
	}
	
	return False;
}
?>