<?php
// Decoding a key from the old cookie
function find_xor_key($decrypted, $encrypted) {
	// Change to original state
	$base64_decoded = base64_decode($encrypted);
	$json_encoded = json_encode($decrypted);
	$outText = '';
	// XOR’ing out key from json_encoded
	for($i=0; $i < strlen($json_encoded); $i++) {
		$outText .= $json_encoded[$i] ^ $base64_decoded[$i % strlen($base64_decoded)];
	} 
	return $outText;
}
$cookie = array("showpassword"=>"no", "bgcolor"=>"#ffffff");
$key = find_xor_key($cookie, "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=");
print "XOR Key: " . $key . "\n";
?>