<script lang="ts">
    import { goto } from '$app/navigation';
    
    let email = '';
    let password = '';
    let password2 = '';
    let errorMessage = '';

    async function handleRegister(event: SubmitEvent) {
        event.preventDefault();
        errorMessage = '';

        // Şifre kontrolü
        if (password !== password2) {
            errorMessage = 'Passwords do not match';
            return;
        }

        try {
            const response = await fetch('http://0.0.0.0:8000/api/users/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({ 
                    email, 
                    password 
                })
            });

            const result = await response.json();

            if (!response.ok) {
                errorMessage = result.email?.[0] || result.password?.[0] || 'Registration failed';
                return;
            }

            if (result.token) {
                localStorage.setItem('token', result.token);
                await goto('/');
            } else {
                errorMessage = 'Registration successful but no token received';
            }

        } catch (error) {
            console.error('Registration error:', error);
            errorMessage = 'An error occurred during registration';
        }
    }
</script>

<div class="register-container">
    <h1>Register</h1>

    {#if errorMessage}
        <div class="error-message">
            {errorMessage}
        </div>
    {/if}

    <form on:submit={handleRegister} class="register-form">
        <div class="form-group">
            <label for="email">Email</label>
            <input
                type="email"
                id="email"
                bind:value={email}
                placeholder="Enter your email"
                required
            />
        </div>

        <div class="form-group">
            <label for="password">Password</label>
            <input
                type="password"
                id="password"
                bind:value={password}
                placeholder="Enter your password"
                required
            />
        </div>

        <div class="form-group">
            <label for="password2">Confirm Password</label>
            <input
                type="password"
                id="password2"
                bind:value={password2}
                placeholder="Confirm your password"
                required
            />
        </div>

        <button type="submit">Register</button>

        <div class="login-link">
            Already have an account? 
            <a href="/login">Login here</a>
        </div>
    </form>
</div>

<style>
    .register-container {
        max-width: 400px;
        margin: 4rem auto;
        padding: 2rem;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        border-radius: 8px;
        background-color: white;
    }

    h1 {
        text-align: center;
        margin-bottom: 2rem;
        color: #333;
    }

    .register-form {
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
    }

    .form-group {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    label {
        font-weight: 500;
        color: #555;
    }

    input {
        padding: 0.75rem;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 1rem;
    }

    input:focus {
        outline: none;
        border-color: #007bff;
        box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
    }

    button {
        padding: 0.75rem;
        background-color: #28a745;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.2s;
    }

    button:hover {
        background-color: #218838;
    }

    .error-message {
        padding: 0.75rem;
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
        border-radius: 4px;
        margin-bottom: 1rem;
    }

    .login-link {
        text-align: center;
        font-size: 0.9rem;
        color: #666;
    }

    .login-link a {
        color: #007bff;
        text-decoration: none;
    }

    .login-link a:hover {
        text-decoration: underline;
    }
</style> 