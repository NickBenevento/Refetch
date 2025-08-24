import ProductList from "./ProductList";
import AddProduct from "./ProductAdd";

const ProductsPage = () => {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Our Products</h1>
      <ProductList />
      <AddProduct />
    </div>
  );
};

export default ProductsPage;
