import Image from "next/image";

interface ProductCardProps {
  imageUrl: string;
  title: string;
  price: string;
}

const ProductCard: React.FC<ProductCardProps> = ({
  imageUrl,
  title,
  price,
}) => {
  return (
    <div className="w-64 bg-white shadow-md rounded-lg overflow-hidden">
      <Image
        src={imageUrl}
        alt={title}
        width={256}
        height={320}
        className="w-full h-64 object-cover"
        unoptimized={true} // Add this to fix the issue
      />
      <div className="p-4 text-center">
        <h2 className="text-lg font-semibold">{title}</h2>
        <p className="text-gray-500">{price}</p>
      </div>
    </div>
  );
};

export default ProductCard;
