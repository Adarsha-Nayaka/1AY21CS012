import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ProductDetail = ({ match }) => {
    const [product, setProduct] = useState(null);

    useEffect(() => {
        const fetchProductDetails = async () => {
            const response = await axios.get(`/api/categories/${match.params.category}/products/${match.params.productId}`);
            setProduct(response.data);
        };
        fetchProductDetails();
    }, [match.params.category, match.params.productId]);

    if (!product) return <div>Loading...</div>;

    return (
        <div>
            <h1>{product.name}</h1>
            <p>{product.description}</p>
            <p>Price: {product.price}</p>
        </div>
    );
};

export default ProductDetail;
