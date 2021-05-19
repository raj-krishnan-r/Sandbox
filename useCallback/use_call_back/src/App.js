import React, { useCallback, useState } from 'react';

const App = () => {
   const [name, setName] = useState('');
   const [num1, setNum1] = useState(0);
   const [num2, setNum2] = useState(0);
   const ans = useCallback(()=>{
    adder(num1,num2)
   },[num2, num1]);
   return (
      <div>
         <input
            placeholder="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
         />
         <input
            placeholder="Value 1"
            value={num1}
            onChange={(e) => setNum1(e.target.value)}
         />
         <input
            placeholder="Value 2"
            value={num2}
            onChange={(e) => setNum2(e.target.value)}
         />
         {ans}
      </div>
   );
};

const adder = (a1, a2) => {
   console.log('Adding numbers');
   return parseInt(a1) + parseInt(a2);
};

export default App;