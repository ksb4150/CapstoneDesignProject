<?php
  $conn = mysqli_connect("localhost", "root", "qwpo1209", "ccan");

  //include("mysqlcon.php");

  $data[] = array('Sec','ID', 'Count',"Flag","Amount");
  $sql = "select * from can;";
  //WHERE NOT(Count = 0);
  $query_res = mysqli_query($conn, $sql);

  while($result = mysqli_fetch_array($query_res)) {
    $data[] = array((float)$result['Sec'],$result['ID'], (int)$result['Count'], (int)$result['Flag'],(int)$result['Amount']);
  }

  //echo $data;
  //echo $data[0][1];
  echo json_encode($data, JSON_UNESCAPED_UNICODE);

  mysqli_close($conn);
 ?>
