import logo from './logo.svg';
import './App.css';
import { render, screen, fireEvent } from '@testing-library/react';
import { useState } from 'react';


fireEvent.click(button);
expect(button).toHaveStyle({ backgroundColor: 'blue' });
expect(button.textContent).toBe('change to red!');
const [buttonColor, setColor] = useState('red');




function App() {
  return (
    <div>
      <button style={{backgroundColor: 'red'}}>change to blue!</button>
    </div>

    
  );
}

export default App;
