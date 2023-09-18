/*This code defines an output called alb_public_url with the description "Public URL for Application Load Balancer" 
and the value of the DNS name of the Application Load Balancer. This output can be used to get the public URL of the 
Application Load Balancer after Terraform has been applied. */
# Terraform Outputs
output "alb_public_url" {
  description = "Public URL for Application Load Balancer"
  value       = aws_lb.alb.dns_name
}
