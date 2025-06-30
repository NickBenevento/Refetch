import type { Product } from "../../api/types/products";
import { useEffect, useState } from "react";
import ProductCard from "./ProductCard";
import ky, { HTTPError } from "ky";

const getProducts = async (): Promise<Product[]> => {
  try {
    return await ky.get("").json<Product[]>();
  } catch (error) {
    if (error instanceof HTTPError) {
      console.error("HTTP error:", error.response.status);
    } else {
      console.error("Network or unexpected error:", error);
    }
    return []; // Fallback to empty list
  }
};

const ProductList = () => {
  const [products, setProducts] = useState<Product[] | null>(null);

  useEffect(() => {
    async () => {
      const data = await getProducts();
      setProducts(data);
    };
  }),
    [];

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
