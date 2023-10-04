from models import KHAINIEM
import os
import django

def configure_django_settings():
    # Replace 'your_project_name.settings' with the actual path to your project's settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oop.settings')

# Call the function to configure Django settings
configure_django_settings()
def insert_data():
    # Insert data into the table
    kn1 = KHAINIEM(MA_KNIEM='kn1', TEN_KTHUC='Lớp', TU_KHOA='Lớp, lớp', ND_KTHUC='''<h2> Lớp là gì? </h2>
<hr>
Một lớp là một bản thiết kế cho đối tượng. Chúng ta có thể coi một lớp như một bản phác thảo của một ngôi nhà với các chi tiết. Nó chứa tất cả các chi tiết về tên, màu sắc, kích thước,..
<br>Dựa trên những mô tả này, chúng ta có thể xây dựng các ngôi nhà. Ở đây, một ngôi nhà là một đối tượng. Tức là bạn có thể sử dụng bản thiết kế (hay lớp này) để định nghĩa bao nhiêu đối tượng tùy thích. Hoặc quay lại ví dụ trên, khi ta sử dụng kiểu dữ liệu danh sách list, chúng ta thấy rằng chúng ta có thể khai báo và sử dụng bao nhiêu danh sách với các phần tử khác nhau tùy thích.
<br>Các định nghĩa và các phương thức đã được định nghĩa sẵn trong các lớp List tương ứng và chúng ta chỉ việc tạo ra các đối tượng và tận dụng lại được tất các các phép toán và hành động có thể trên các đối tượng này.
''', MA_LKET='none')
    kn1.save()
insert_data()