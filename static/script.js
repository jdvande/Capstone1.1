// Define a function to toggle the visibility of a password field.
function togglePasswordVisibility(passwordFieldId, toggleIcon) {
  // Get the DOM element for the password field using its ID.
  var passwordField = document.getElementById(passwordFieldId);

  // Check if the current type of the password field is 'password'.
  if (passwordField.type === "password") {
    // If it is 'password', change the type to 'text' to show the password.
    passwordField.type = "text";
    // Remove the 'fa-eye' class to change the icon to an open eye (visible).
    toggleIcon.classList.remove('fa-eye');
    // Add the 'fa-eye-slash' class to change the icon to a slashed eye (indicating visibility).
    toggleIcon.classList.add('fa-eye-slash');
  } else {
    // If the type is not 'password', change it back to 'password' to hide the text.
    passwordField.type = "password";
    // revert the icon to the slashed eye (hidden).
    toggleIcon.classList.remove('fa-eye-slash');
    // change the icon back to an open eye.
    toggleIcon.classList.add('fa-eye'); 
  }
}

  // This ensures the script runs after the DOM is fully loaded.
document.addEventListener('DOMContentLoaded', (event) => {


// Listener for the registration form submission
var registerForm = document.getElementById('register');
if (registerForm) {
  registerForm.addEventListener('submit', function(event){
    event.preventDefault();

    var newUsername = document.getElementById('new-username').value;
    var newPassword = document.getElementById('password').value; // Corrected ID
    var confirmPassword = document.getElementById('confirm-password').value;
    var passwordError = document.getElementById('password-error');

    // Check if the passwords match
    if(newPassword !== confirmPassword){ // Use !== for inequality
      // If passwords don't match, show the error
      passwordError.style.display = 'block';
    } else {
      // If passwords match, hide the error and proceed
      passwordError.style.display = 'none';
      alert('User successfully created');

      // Log new username and password
      console.log("New Username: " + newUsername);
      console.log("New Password: " + newPassword);

      // Redirect to login on successful registration
      window.location.href = 'login.html';
    }
  });
}


  // Listener for the "Create New User" button click
  var createUserButton = document.getElementById('createUser');
  if (createUserButton) {
    createUserButton.addEventListener('click', function(){
      // Redirect to the registration page
      window.location.href = 'register.html';
    });
  }
});

<script>
function updateValue(slider) {
  var valueDisplay = document.getElementById(slider.id + '-value');
  valueDisplay.textContent = slider.value;
}

function updateParameterArray() {
  var sliders = document.querySelectorAll('input[type="range"]');
  var parametersArray = [];
  var displayText = 'Slider Values: ';

  sliders.forEach(function(slider) {
    parametersArray.push(slider.value);
  });

  displayText += '<br>' + parametersArray.join(', ');
  document.getElementById('parameterValuesDisplay').textContent = displayText;
}

document.addEventListener('DOMContentLoaded', function() {
  var sliders = document.querySelectorAll('input[type="range"]');
  sliders.forEach(function(slider) {
    slider.addEventListener('input', function() {
      updateValue(this);
    });
    updateValue(slider);
  });

  document.getElementById('generateButton').addEventListener('click', function() {
    updateParameterArray();
  });
});
</script>
