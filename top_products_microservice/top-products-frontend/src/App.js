import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import ProductList from './components/ProductList';
import ProductDetail from './components/ProductDetail';

function App() {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/categories/:category/products/:productId" element={<ProductDetail />} />
                <Route path="/categories/:category/products" element={<ProductList />} />
                <Route path="/" element={<h1>Welcome to the Top Products Comparison Site</h1>} />
            </Routes>
        </Router>
    );
}

export default App;
