<script>
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';
    let user = null;
    async function verifyUser() {
        const token = localStorage.getItem('token');
        if (!token) {
            goto('/login');
            return;
        }
        try {
            const response = await fetch('http://0.0.0.0:8000/api/users/user/', {
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
            });

            console.log('Token:', token);
            console.log('Response status:', response.status);

            if (response.ok) {
                user = await response.json();
                console.log('User data:', user);
            } else {
                console.log('Response not ok:', await response.text());
                goto('/login');
            }
        } catch (error) {
            console.error('Verification error:', error);
            goto('/login');
        }
    }

    onMount(verifyUser);
</script>

{#if user}
    <header class="header">
        <div class="user-info">
            <span>Welcome, {user.email}</span>
            <button on:click={() => {
                localStorage.removeItem('token');
                goto('/login');
            }}>Logout</button>
        </div>
    </header>
{/if}

<div class="todo-container">
  <h1>Todo List</h1>

  <form  class="todo-form">
    <input
      type="text"
      placeholder="Add a new todo..."
      required
    />
    <button type="submit">Add</button>
  </form>

  <ul class="todo-list">
<!--     {#each todos as todo (todo.id)}
      <li class="todo-item" class:completed={todo.completed}>
        <input
          type="checkbox"
          checked={todo.completed}
          on:change={() => toggleTodo(todo.id, todo.completed)}
        />
        <span>{todo.title}</span>
        <button on:click={() => deleteTodo(todo.id)}>Sil</button>
      </li>
    {/each} -->
  </ul>
</div>

<style>
  .todo-container {
    max-width: 600px;
    margin: 2rem auto;
    padding: 1rem;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    border-radius: 8px;
  }

  .todo-form {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
  }

  .todo-form input {
    flex: 1;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
  }

  .todo-form button {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  .todo-list {
    list-style: none;
    padding: 0;
  }

  .todo-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 0.5rem;
    border-bottom: 1px solid #eee;
  }

  .todo-item.completed span {
    text-decoration: line-through;
    color: #888;
  }

  .todo-item button {
    margin-left: auto;
    padding: 0.25rem 0.5rem;
    background-color: #dc3545;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  .header {
    background-color: #f8f9fa;
    padding: 1rem;
    margin-bottom: 2rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  .user-info {
    max-width: 600px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .user-info button {
    padding: 0.5rem 1rem;
    background-color: #dc3545;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  .user-info button:hover {
    background-color: #c82333;
  }
</style>
