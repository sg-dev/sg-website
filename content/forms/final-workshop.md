---
title: "Final Workshop Form"
url: "/final-workshop-form/"
---

<style>
    form {
        max-width: 600px;
        margin: 0 auto;
        padding: 1em;
        background: #f9f9f9;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    form input, form select, form button {
        margin-bottom: 1em;
        padding: .5em;
        border: 1px solid #ccc;
        border-radius: 3px;
        width: 100%;
        box-sizing: border-box;
    }
    form select {
        appearance: none;
        -webkit-appearance: none;
        -moz-appearance: none;
        background-image: url("data:image/svg+xml;utf8,<svg fill='black' height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'><path d='M7 10l5 5 5-5z'/><path d='M0 0h24v24H0z' fill='none'/></svg>");
        background-repeat: no-repeat;
        background-position-x: 98%;
        background-position-y: 50%;
    }
    form button {
        background: #007BFF;
        color: white;
        border: none;
        cursor: pointer;
    }
    form button:hover {
        background: #0056b3;
    }
    form label {
        margin-bottom: .5em;
        color: #333333;
        display: block;
        font-weight: bold;
    }
    
	label.required:after {
        content: "*";
        color: red;
      }

</style>
<form action="https://submit-form.com/BxIceJb8v" method="POST">

<input
type="hidden"
name="_redirect"
value="https://www.sg.ethz.ch/forms/thanks"
/>

<label for="first_name" class="required">First Name</label>
<input type="text" id="first_name" name="first_name" placeholder="Enter your first name" required>

<label for="last_name" class="required">Last Name</label>
<input type="text" id="last_name" name="last_name" placeholder="Enter your last name" required>


<label for="title" class="required">Title</label>
<select id="title" name="title" required>
    <option value="">Select your title</option>
    <option value="Mr">Mr.</option>
    <option value="Ms">Ms.</option>
    <option value="Dr">Dr.</option>
    <option value="Prof">Prof.</option>
</select>

<label for="institution" class="required">Institution</label>
<input type="text" id="institution" name="institution" placeholder="Enter your institution" required>

<label for="city" class="required">City</label>
<input type="text" id="city" name="city" placeholder="Enter your city" required>

<label for="email" class="required">Email</label>
<input type="email" id="email" name="email" placeholder="Enter your email" required>

<button type="submit">Submit</button>
</form>
