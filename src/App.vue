<template class = "whole-website">
  <div class = "car-picture">
      
      <img alt="car" src="./assets/lambo.png">
  </div>
  <div class = "welcome-message">
    <p>Our program aims to help prevent the loss of lives due to vehical accidents.</p>
  </div>
  <div class = "continue-button">
  <button v-on:click="">Continue</button>
  </div>
</template>
 
<script>
export default{

}
</script>

 <style>
body, html{
  margin: 0;
  width:100%;
}
html{
  background-color: dark-grey;
}
img {
  object-fit: contain;
  }
  .whole-website{
  font-family: Montserrat;
  align-items: center;
}
  .welcome-message{
  margin-top: 130%;
  margin-left: 15px;
  margin-right: 15px;
  color: white;
  text-align: center;
  font-size: 29px;
}
  .continue-button
  {
    text-align: center;
    margin-top: 20%;
    color:#fff;
  }
.car-picture{
  margin-top: 90%;
  margin-left: auto;
  margin-right: auto;
  align-text: center;
}
</style> 