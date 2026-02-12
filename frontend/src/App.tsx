import { Component, createSignal, onMount } from 'solid-js';

type Item = {
  id: int;
  title: string;
  completed: bool;
};

const App: Component = () => {
  const [items, setItems] = createSignal<Item[]>([]);
  const [newItemTitle, setNewItemTitle] = createSignal('');

  const fetchItems = async () => {
    try {
      const res = await fetch('/items/');
      if (res.ok) {
        const data = await res.json();
        setItems(data);
      }
    } catch (e) {
      console.error(e);
    }
  };

  const addItem = async () => {
    if (!newItemTitle()) return;
    try {
      const res = await fetch('/items/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: newItemTitle() }),
      });
      if (res.ok) {
        const newItem = await res.json();
        setItems([...items(), newItem]);
        setNewItemTitle('');
      }
    } catch (e) {
      console.error(e);
    }
  };

  const toggleItem = async (id: number, completed: boolean) => {
    try {
      // Optimistic update
      setItems(items().map(i => (i.id === id ? { ...i, completed } : i)));

      const res = await fetch(`/items/${id}?completed=${completed}`, {
        method: 'PUT',
      });
      if (!res.ok) {
        // Revert on error
        setItems(items().map(i => (i.id === id ? { ...i, completed: !completed } : i)));
      }
    } catch (e) {
      console.error(e);
    }
  };

  onMount(fetchItems);

  return (
    <div class="container">
      <h1>Checklist</h1>
      <div class="input-group">
        <input
          type="text"
          placeholder="Add a new task..."
          value={newItemTitle()}
          onInput={(e) => setNewItemTitle(e.currentTarget.value)}
          onKeyDown={(e) => e.key === 'Enter' && addItem()}
        />
        <button class="add-btn" onClick={addItem}>Add</button>
      </div>
      <ul>
        {items().map((item) => (
          <li class={item.completed ? 'completed' : ''}>
            <input
              type="checkbox"
              checked={item.completed}
              onChange={(e) => toggleItem(item.id, e.currentTarget.checked)}
            />
            <span>{item.title}</span>
            {/* Delete functionality not in backend yet, so omitted */}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
