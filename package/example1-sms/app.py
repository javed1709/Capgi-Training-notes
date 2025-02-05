import Admin.service
Admin.service.admin_service()

import Admin.product
Admin.product.admin_product()

import Admin.Common.header
Admin.Common.header.admin_common_header()

import Admin.Common.footer
Admin.Common.footer.admin_common_footer()

print(isinstance(Admin.service.admin_service(), type(Admin.service.admin_service())))

# should we create init in every folder?