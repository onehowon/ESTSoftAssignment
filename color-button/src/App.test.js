import { render, screen } from '@testing-library/react';
import App from './App';


test('버튼이 제대로 잘 작동하고 있습니까?', () => {
  render(<App />);
  
	const button = screen.getByRole('button', { name: 'change to blue!' });
  
	expect(button).toHaveStyle({ backgroundColor: 'red' });

  fireEvent.click(button);
  expect(button).toHaveStyle({ backgroundColor: 'blue' });
  expect(button.textContent).toBe('change to red!');

  const [buttonColor, setColor] = useState('red');
  const newColor = buttonColor === 'red' ? 'blue' : 'red';

  return (
    <div>
      <button style={{ backgroundColor: buttonColor }} 
      onClick={() => setColor(newColor)}>change to {newColor}!</button>
    </div>
);
});
