import React from 'react';import{createRoot}from'react-dom/client';import ProductCard from'./ProductCard.jsx';import'./styles.css';
const product={id:7,title:'Wireless Headphones',description:'Clear sound and long battery life.',category:'Electronics',rating:4.5,price:79.99,inStock:true,image:'./headphones.png'}
createRoot(document.getElementById('root')).render(<main><h1>Product Card</h1><ProductCard product={product} onAddToCart={(item,quantity)=>alert(`${quantity} × ${item.title} added`)}/></main>)
