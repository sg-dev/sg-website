---
title: "Registration Confirmed"
---
<div id="registration-info"></div>

<script>
    // Function to get query parameters and format them nicely
    function getQueryParams() {
        const params = new URLSearchParams(window.location.search);
        
        // Extract values from query parameters
        // const firstName = params.get('first_name') || '';
        const lastName = params.get('last_name') || '';
        const title = params.get('title') || '';

        // Format the output
        return `Thank you for registering <strong>${title} ${lastName}</strong>.`;
    }

    // Render the registration info
    document.getElementById('registration-info').innerHTML = getQueryParams();
</script>


You can find the **[Event Program here](/events/sg-final-symposium-october-2024/)**.