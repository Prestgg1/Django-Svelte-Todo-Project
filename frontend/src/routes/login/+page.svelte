<script lang="ts">
      import { goto } from '$app/navigation';  // Bu satırı en üste ekleyin
  let email = '';
  let password = '';

  async function handleLogin(event: SubmitEvent) {
    event.preventDefault();
    
    try {
      // API call will be made here
      const response = await fetch('http://127.0.0.1:8000/api/users/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({ email, password })
      });
      const result = await response.json();
      console.log('Login response:', result);
      
      if (!result.token) {
        console.error('Token alınamadı:', result);
        return;
      }
      
      localStorage.setItem('token', result.token);
      console.log('Saved token:', localStorage.getItem('token'));
      await goto('/');
      
    } catch (error) {
      console.error('Login error:', error);
    }
  }
</script>

<div class="login-container">
  <h1>Login</h1>
  
  <form on:submit={handleLogin} class="login-form">
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

    <button type="submit">Login</button>
  </form>
</div>

<style>
  .login-container {
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

  .login-form {
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
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  button:hover {
    background-color: #0056b3;
  }
</style> 