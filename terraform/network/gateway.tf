resource "aws_internet_gateway" "stage-gw" {
    vpc_id = aws_vpc.stage-vpc.id
    tags = {
        Name = "stage-gw"
    }
}
