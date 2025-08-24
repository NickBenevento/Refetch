import { useAtom } from "jotai";
import { productAtom, type Product } from "../../api/types/products";
import { useEffect, useState } from "react";
import ProductCard from "./ProductCard";
import { fetchProducts } from "../../api/fetch/product";

const ProductList = () => {
  const [products, setProducts] = useAtom(productAtom);
  // const [products, setProducts] = useState<Product[] | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchProducts();
      setProducts(data);
    };

    fetchData();
  }, []);

  if (products === null) {
    return <div>Loading products...</div>;
  }

  return (
    <div>
      <h2>Products:</h2>
      {products.length === 0 ? (
        <div>No products available right now.</div>
      ) : (
        products.map((product) => (
          <ProductCard key={product.id_} data={product} />
        ))
      )}
    </div>
  );
};

export default ProductList;
