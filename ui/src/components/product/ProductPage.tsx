import { useAtom } from "jotai";
import { productAtom } from "../../api/types/products";
import ProductList from "./ProductList";
import AddProduct from "./ProductAdd";
import { fetchProducts } from "../../api/fetch/product";
import { useEffect } from "react";

const ProductsPage = () => {
  const [products, setProducts] = useAtom(productAtom);

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchProducts();
      setProducts(data);
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Our Products</h1>
      <ProductList products={products} />
      <AddProduct />
    </div>
  );
};

export default ProductsPage;
