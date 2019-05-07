<?php
// Encoding a new cookie
function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';
    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    	$outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
}
$cookie = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");
$coded_cookie = base64_encode(xor_encrypt(json_encode($cookie)));
print "New Cookie: " . $key . "\n";
?>