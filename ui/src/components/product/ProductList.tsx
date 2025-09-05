import ProductCard from "./ProductCard";
import type { Product } from "../../api/types/products";

interface ProductListProps {
  products: Product[] | null;
}

const ProductList: React.FC<ProductListProps> = (props) => {
  const { products } = props;

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
