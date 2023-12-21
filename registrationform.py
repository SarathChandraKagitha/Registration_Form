<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration Form</title>
</head>
<style>
    body {
        font-family: Lucida Bright;
        background-color: #f4f4f4;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    
    form {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 300px;
    }
    
    section {
        margin-bottom: 2px;
        width: 12px; 
        height: 12px; 
        border: 2px;
    }
    
    input, select {
        width: 100%;
        padding: 8px;
        margin-bottom: 16px;
        box-sizing: border-box;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    
    button {
        background-color: #1fd41f;
        color: white;
        padding: 10px;
        border:  5px;
        border-radius: 4px;
        cursor: pointer;
        width: 100%;
    }
    
    button:hover {
        background-color: #45a049;
    }
    
    .error {
        color: red;
        margin-top: -10px;
        margin-bottom: 10px;
    }
</style>
<body>

    <form id="registrationForm" onsubmit="return validateForm()">
        <label for="firstName">Full Name:</label>
        <input type="text" id="firstName" name="firstName" placeholder="First Name" required>
        <input type="text" id="lastName" name="lastName" placeholder="Last Name" required>

        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" required>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>

        <label for="confirmPassword">Confirm Password:</label>
        <input type="password" id="confirmPassword" name="confirmPassword" required>

        <label for="dob">Date of Birth:</label>
        <input type="date" id="dob" name="dob" required>

        <label for="gender">Gender:</label>
        <select id="gender" name="gender" required>
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
        </select>

        <section>
            <input type="checkbox" id="terms" name="terms" required>
            
        </section>
        <p>I agree to the Terms and Conditions</p>
           
        

        <button type="submit">Register</button>
    </form>
    <script>
        function validateForm() {
            var password = document.getElementById("password").value;
            var confirmPassword = document.getElementById("confirmPassword").value;

            if (password !== confirmPassword) {
                alert("Passwords do not match.");
                return false;
            }

            return true;
        }
    </script>

</body>
</html>
