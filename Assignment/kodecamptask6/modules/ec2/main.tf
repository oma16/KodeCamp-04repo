
resource "aws_instance" "public_instance" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = var.public_subnet_id
  security_groups = [var.public_sg_id]
  key_name      = var.key_name
  

  user_data = file("${path.module}/../../scripts/install_nginx.sh")

  tags = {
    Name = "PublicInstance"
  }
}

resource "aws_instance" "private_instance" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = var.private_subnet_id
  security_groups = [var.private_sg_id]
  key_name      = var.key_name

  user_data = file("${path.module}/../../scripts/install_postgresql.sh")

  tags = {
    Name = "PrivateInstance"
  }
}



